print("""
3、GitHub 目前Git LFS的总存储量为1G左右，超过需要付费。(上传失败时，可以开启VPN进行上传)
4、batch response: Repository or object not found
1$ git lfs push origin master
23Git LFS: (B of 1 files) B/ 207.25 MB
4 Check that it exists and that vou haveeconanryaeng LargefileStorage.git/info/1fs/objects/ba
Check that it exists and that you have proper access to it
失败原因：
1是gitee.com这个git仓库并不支持1fs，所以在大文件入库的时候，提示失败
解决方式
目前来说，GitHub、GitLab、Coding。gitee(也就是git.oschina net)目前还不支持。
""")
