$id_key = '_art'
$insert_var = '%ART_LOCAL_ROOT%'

function parse_line($line){
	$separator = ' '
	$tokens = $line.split($separator)
	# Write-Host 'func: tokens'
	# Write-Host $tokens
	$newline = ''
	foreach ($token in $tokens){
		# found the path token
		$new_token = ''
		$match_tok = '.*'+$id_key+'.*'
		if ($token -match $match_tok){
			$pattern = '(.*)('+$id_key+'.*)'
			$path_tok = '\\\\'
			if ($token -match '.*'+$path_tok+'.*'){
				# do nothing
			}
			else{
				$path_tok = '/'
			}
			$replacement = '"'+$insert_var+$path_tok+'$2";'
			$new_token = $token.trim('";') -replace $pattern, $replacement 
		}else{
			$new_token = $token
		}
		$newline = $newline + $separator + $new_token
		# Write-Host 'func: newline'
		# Write-Host $newline
	}
	$newline.TrimEnd($separator)
	# Write-Host 'func: ret new line'
	# Write-Host $newline
	return
}

$workfile = Read-Host -prompt "Drag and drop the file to be processed here..."
$outfile = $workfile.trim('.ma') + '_processed.ma'

$count = 0
$b_found_proxy = $FALSE
$buffer = ''
foreach ($line in Get-Content $workfile) {
	if ($line -match '.*createNode RedshiftProxyMesh.*'){
		Write-Host 'Found Proxy'
		Write-Host $line
		$b_found_proxy = $TRUE
		$count = 0
	}
	elseif ($b_found_proxy -and $count -lt 1) {
		Write-Host $line
		$count += 1
	} 
	elseif($b_found_proxy){
		Write-Host 'original line'
		Write-Host $line
		$newline = parse_line($line)
		Write-Host 'new line'
		Write-Host $newline
		#Write-Host 'end new line'
		$line = $newline
		$b_found_proxy = $FALSE
	}else{
		#do nothing
	}
	$buffer = $buffer + $line + "`n"
}
Set-Content $outfile $buffer