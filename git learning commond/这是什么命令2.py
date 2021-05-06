print("""
warning: LF will be replaced by CRLF in 解决办法
warning: LF will be replaced by CRLF in
原因是存在符号转义问题
windows中的换行符为 CRLF， 而在linux下的换行符为LF，所以在执行add.时出现提示，解决办法：
git config --global core.autocrlf false
""")
