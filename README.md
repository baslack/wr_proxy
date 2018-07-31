# wr_proxy
## The Wrong Rock - Artella / Redshift path patcher

Author: Benjamin Slack

### Abstract:
This utility was developed in my work on ["The Wrong Rock"](http://heromation.com/project/the-wrong-rock/) 
to deal with some shortcomings of the Artella platform and its use with Redshift Rendering. In a nutshell,
Artella's platform uses an Maya environment variable as the basis of all file paths in the scene. Some Redshift
nodes can use these variables, some can't. To work around the difficulty, we resorted to using system level
environment variables with the effected nodes. Implemented originally in powershell, we quickly moved the 
script to python for performance reasons. Both scripts are included in this package for reference sake.
