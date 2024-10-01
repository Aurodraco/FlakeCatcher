# 雪花捕手

雪花捕手是一款写作和保存零散文字的编辑器，目标是解决创作文字片段每次都需要单独创建和命名文件的麻烦。

这款编辑器采用嵌入式本地数据库（sqlite）存储写入的文字，并结合向量模型（Dmeta-embedding-zh）实时搜索近似的片段显示在右侧界面。
 
## 目录

- [雪花捕手](#雪花捕手)
  - [目录](#目录)
    - [上手指南](#上手指南)
    - [安装步骤](#安装步骤)
    - [开发](#开发)
    - [作者](#作者)
    - [版权说明](#版权说明)

### 上手指南

像其他编辑器一样在左侧文本框编辑即可

右键点击右侧界面有导出和设置等选项

光标在最前方时，Ctrl + up（上方向键）可以读取上次打开时写入的文字片段

### 安装步骤

1. 找到项目的release界面下载对应的文件

2. 解压到合适的目录，找到 雪花捕手.exe 并运行

### 开发

1. 准备好python环境，克隆项目到本地

```
git clone https://github.com/Aurodraco/FlakeCatcher.git
```

3. 下载用到的[向量模型](https://huggingface.co/DMetaSoul/Dmeta-embedding-zh)，保存在项目根目录下，并命名为`Dmeta-embedding-zh`

4. 项目采用poetry管理，代码量少且简单，基本上不需要编程基础就能阅读和修改，你可以根据自己的喜好做出修改

### 作者

Bilibili: 肆星Auro

### 版权说明

该项目签署了MIT 授权许可，详情请参阅[LICENSE](https://github.com/Aurodraco/FlakeCatcher/blob/main/LICENSE)
