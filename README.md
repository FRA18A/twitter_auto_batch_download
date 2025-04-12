# twitter_auto_batch_download
半自动免费推特批量下载用户上传的图片，需要Bulk Image Downloader作为辅助

需要：chrome，python，Bulk Image Downloader

1.首先打开那个人的主页，F12网页，刷新然后下拉至完全加载（建议单击鼠标中键然后向下拖）network下点击Img，然后上面有一个小下载，下载har文件。
2.把.py的har_file_path改成har文件的位置，执行之后在downloaded_images里找到一堆output文件，为了免费版的Bulk Image Downloader设置成99个图一个文件。
3.依次把txt文件拖进Bulk Image Downloader点击下载。
