# Pscbo1 — 照片与文字

个人网站，发布地址：https://pscbo1.github.io/

首页保留四张照片；摄影沿用原来的六组编排，包括安提瓜风筝节和2024深山拜年视频；文字为小村记述和Patriarchy译文，注明National Geographic原文来源。2024个人选集与原摄影标注仅保存在个人本地归档中。

## 更新

编辑 content/ 中的HTML和资源文件，然后运行：

```sh
python build.py --release
```

修改并提交 main 后，GitHub Actions 会自动构建并发布 dist。gh-pages 是初次发布时的历史分支，不再作为更新入口。无需WordPress、npm或数据库。

具体操作见 [自己更新网站](更新说明.md)。

默认 `python build.py` 生成带 noindex 的审阅版本；`--release` 使用已批准的发布开关并允许搜索引擎索引。

## 视频和素材

安提瓜风筝节使用本地MP4；深山拜年使用本地封面和点击后加载的YouTube播放器，并提供Bilibili和YouTube原页入口。后者的4K成片及个人归档保留在本地，不在本仓库。平台播放器受访问网络和平台可用性影响。

字体与图片均由本站提供。网页图片是派生副本；完整WordPress备份、私人文字、Other Works、Memories 6和个人存档不属于本仓库。
