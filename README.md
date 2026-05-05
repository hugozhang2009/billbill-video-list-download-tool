# Billbill 视频目录提取工具

本工具支持自动从 Bilibili 视频页面中提取分 P（Part）列表，便于批量分析和整理视频目录信息。适用于需要获取 B 站分集标题、方便整理或批量下载剧集信息的场景。

## 功能简介

- 输入 Bilibili 视频 URL，自动获取该视频所有分集（P）的标题及顺序。
- 支持自动设置请求头，模拟浏览器访问，提升页面获取成功率。
- 把 HTML 源码保存为本地文件，便于后续分析与备份。
- 操作简单，无需手动网页操作，只需修改一行代码即可运行。

## 代码实现说明

1. **请求视频页面数据**  
   使用 `requests` 库发送 GET 请求，通过自定义浏览器 User-Agent 和 Referer，有效规避反爬虫措施。

2. **分析 HTML 提取目录数据**  
   利用 `BeautifulSoup` 找到页面中的 `window.__INITIAL_STATE__` 脚本数据块，将其解析为 JSON，从中读取所有分集（P）的标题。

3. **保存 HTML 页面源码**  
   自动将抓取到的页面源码以 `Bilibili视频目录_时间戳.txt` 格式保存，保留数据快照，方便调试与溯源。

4. **打印分集目录到控制台**  
   按序输出每一集的序号及名称，例如：`P1 第一话`、`P2 第二话` 等。

## 使用方法

1. 安装依赖：

   ```bash
   pip install requests beautifulsoup4
   ```

2. 打开并编辑 `billbill video list download tool.py`，找到下面这行代码：
   
   ```python
   url = "https://www.bilibili.com/video/BV1Qi4y1R7tW"
   ```
   
   将等号右侧的 URL 更换为你希望解析的 B 站视频页面链接。

3. 运行脚本：

   ```bash
   python billbill\ video\ list\ download\ tool.py
   ```

4. 查看结果：
    - 控制台将打印所有分集标题。
    - 项目目录下会生成形如 `Bilibili视频目录_20260505153021.txt` 的网页源码文件。

## 注意事项与建议

- 仅支持公开可访问的 Bilibili 正常视频链接，不适用于会员、付费或隐私视频。
- 每次运行都会覆盖上一次生成的同名 txt 文件（如有）。
- 若遇爬取失败或页面结构变化，可参考注释中的知乎及 CSDN 文章查找解决方法并及时维护解析逻辑。
- 请勿用于违反 B 站相关规定的用途，合理合规使用工具。

## 参考资料

- [知乎专栏-解析 Bilibili 播单](https://zhuanlan.zhihu.com/p/117569614)
- [CSDN 博客-含源码分析](https://blog.csdn.net/weixin_42914706/article/details/129112667)
