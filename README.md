# Pscbo1 — 个人网站第二版（本地审阅）

只承载个人表达，不含求职作品集入口。原排版完整留存在本地，网站源文件与私人存档分开。

结构：首页（旧首页四张照片原顺序）、摄影（原照片组合＋安提瓜风筝节视频）、文字（小村记述、国家地理试译）。2024 选集是次级入口。

安提瓜探索经验集暂不放入网站。Other Works 和 memories_6 仅本地留档。Notion 风景摄影尚未完成导入。

## 本地查看与更新

运行 `python build.py` 生成 dist/，直接打开 dist/index.html 即可浏览。
文章、照片编排在 content/*.html，使用简单 HTML；资源在 content/assets/。
修改 content 后再次运行 build.py。不需要 npm、WordPress 或数据库。

## GitHub 与发布

预计使用 pscbo1.github.io 免费网址。目前尚未公开发布。
本仓库若创建，将先保持私有且不开启 Pages；确认公开内容后，才准备发布目录和开启 Pages。
当前 content/site.json 的 publication_approved=false，构建带 noindex 标记；--release 被禁止。
不要上传电脑上的完整 WordPress 备份、review、work、个人留档或数据库。

## 保留说明

页面照片分组、次序与原图比例来源于原站；主题框架改为独立静态 CSS。
Google 字体已放在本地，网页运行不依赖原域名。视频保留原文件，不自动播放。
图片为适合网页浏览的派生副本，原图和历史版本保留于 E 盘主备份。
