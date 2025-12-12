# Tech-Business PowerPoint Template (科技商业演示模板)

## 概述 / Overview

本模板基于仓库中原有的"强磁场高增益托卡马克 [自动保存的].pptx"改造而成，采用现代科技商业风格，适用于技术演示、商业提案、学术汇报等场景。

This template is transformed from the original "强磁场高增益托卡马克 [自动保存的].pptx" file in the repository, featuring a modern tech-business style suitable for technical presentations, business proposals, and academic reports.

## 变更清单 / Change List

### 新增文件 / New Files
- `tech-business-template.pptx` - 基于原文件改造的模板（保留原始内容）
- `tech-business-master-template.pptx` - 全新创建的母版模板（包含多种版式）
- `preview.png` - 模板首页预览图
- `original-screenshot.png` - 原始参考截图（占位符）
- `original-strong-field-backup.pptx` - 原始文件备份
- `transform_ppt.py` - PPT转换脚本
- `README.md` - 本说明文档

### 主要改动 / Key Changes
1. **颜色方案** - 应用统一的科技商业配色
2. **字体规范** - 标准化中英文字体及大小
3. **版式优化** - 16:9 宽屏格式，优化页边距
4. **可编辑性** - 所有文本保持可编辑状态（未栅格化）
5. **母版布局** - 创建多种可复用的版式模板

## 风格规范 / Style Specifications

### 配色方案 / Color Scheme
```
主色 / Primary:     #0B3B71 (RGB: 11, 59, 113)   - 深蓝色，用于标题和强调
辅色 / Secondary:   #0CAAAA (RGB: 12, 170, 170)  - 青色，用于副标题和图表
背景色 / Background: #F5F7FA (RGB: 245, 247, 250) - 浅灰色，柔和背景
文本色 / Text:      #333333 (RGB: 51, 51, 51)    - 深灰色，正文文本
白色 / White:       #FFFFFF (RGB: 255, 255, 255) - 用于深色背景上的文字
```

### 字体规范 / Font Specifications

#### 推荐字体 / Recommended Fonts
- **中文 / Chinese**: 
  - 首选: Noto Sans CJK SC / PingFang SC
  - 备选: Source Han Sans / SimSun
- **英文 / English**: 
  - 首选: Montserrat / Arial
  - 备选: Helvetica / Sans-serif

#### 字号规范 / Font Sizes
| 用途 / Usage | 字号 / Size | 粗细 / Weight |
|-------------|------------|--------------|
| 主标题 / Main Title | 56-64pt | 加粗 / Bold |
| 副标题 / Subtitle | 32-40pt | 常规 / Regular |
| 节标题 / Section Title | 48pt | 加粗 / Bold |
| 正文 / Body Text | 22-28pt | 常规 / Regular |
| 项目符号 / Bullets | 20-24pt | 常规 / Regular |

### 版式规范 / Layout Specifications
- **幻灯片比例 / Aspect Ratio**: 16:9 (13.333" × 7.5")
- **页边距 / Margins**: 
  - 左右 / Left-Right: 2.54cm (1 inch)
  - 上下 / Top-Bottom: 1.9cm (0.75 inch)
- **行间距 / Line Spacing**: 1.2-1.3倍行高
- **段落间距 / Paragraph Spacing**: 6-8pt

### 版式类型 / Layout Types
模板提供以下版式（在 `tech-business-master-template.pptx` 中）：

1. **标题页 / Title Slide** - 用于封面，包含主标题和副标题
2. **目录页 / TOC Slide** - 用于内容概览
3. **内容页 / Content Slide** - 标准单栏内容布局
4. **双栏页 / Two-Column Slide** - 左右分栏对比展示
5. **结论页 / Conclusion Slide** - 深色背景，强调总结

## 使用方法 / How to Use

### 方法一：基于现有内容修改
1. 打开 `tech-business-template.pptx`（包含原始内容的改造版本）
2. 编辑文本、图片等内容
3. 保持统一的字体和配色方案

### 方法二：使用母版模板
1. 打开 `tech-business-master-template.pptx`
2. 选择所需的版式布局
3. 添加自己的内容
4. 复制版式到其他演示文稿

### 方法三：应用到现有PPT
1. 打开您的现有PowerPoint文件
2. 在"设计"选项卡中，选择"浏览主题"
3. 选择 `tech-business-master-template.pptx` 作为主题
4. 根据需要调整内容以匹配新样式

### 使用Python脚本自动转换
```bash
cd presentations/tech-business
python3 transform_ppt.py
```

## 字体安装 / Font Installation

为了确保演示文稿在不同设备上显示一致，建议安装推荐字体。

### Linux (Ubuntu/Debian)
```bash
# 安装 Noto Sans CJK
sudo apt-get install fonts-noto-cjk

# 或下载并安装 Montserrat
# 访问 https://fonts.google.com/specimen/Montserrat
```

### macOS
```bash
# 系统已包含 PingFang SC
# 可从 Google Fonts 下载 Montserrat
```

### Windows
```
PingFang SC 可能不可用，建议使用 Microsoft YaHei 或 SimSun
从 Google Fonts 下载并安装 Montserrat
```

## 注意事项 / Important Notes

### 合并前检查 / Pre-Merge Checklist
1. **字体检查** - 确认本地已安装推荐字体，否则可能显示为默认字体
2. **字体许可** - 本模板推荐的字体（Noto Sans CJK, Arial）均为开源或系统自带
3. **可编辑性** - 所有文本均保持可编辑状态，未转换为图片
4. **兼容性** - 使用 PowerPoint 2016 或更高版本打开以获得最佳效果
5. **文件大小** - 如需减小文件大小，请压缩图片（如有）

### 已知限制 / Known Limitations
1. **字体嵌入** - 未嵌入中文字体（文件会过大），请确保目标设备已安装推荐字体
2. **图标资源** - 模板使用文本和基本形状，未包含矢量图标库
3. **图表样式** - 需要手动调整图表配色以匹配主题

### 未完成事项 / Incomplete Items
- [ ] .potx 格式模板文件（PowerPoint 模板格式）- 需要 Windows/macOS 上的 PowerPoint 完整版创建
- [ ] 高级动画效果 - 保持简洁，未添加复杂动画
- [ ] 自定义矢量图标集 - 建议从 Flaticon 或类似网站获取符合许可的图标

## 文件引用 / File References

### 原始文件 / Original Files
- **源文件路径**: `/强磁场高增益托卡马克 [自动保存的].pptx` (repository root)
- **备份路径**: `presentations/tech-business/original-strong-field-backup.pptx`
- **备份创建时间**: 改造前自动备份

### 参考资料 / References
- 视觉参考: `original-screenshot.png`（用户提供的截图参考）
- 转换脚本: `transform_ppt.py`

## 维护者信息 / Maintainer Information

**创建者 / Creator**: GitHub Copilot Agent  
**创建日期 / Created**: 2025-12-12  
**基于 / Based on**: LouisNuh/dotfiles repository  
**用途 / Purpose**: 提供可复用的科技商业风格 PowerPoint 模板

## 技术细节 / Technical Details

### 使用的工具和库 / Tools and Libraries
- **Python 3.12.3**
- **python-pptx 1.0.2** - PowerPoint 文件处理
- **Pillow 12.0.0** - 图像处理和预览生成

### 脚本说明 / Script Description
`transform_ppt.py` 执行以下操作：
1. 加载原始 PPTX 文件
2. 设置 16:9 幻灯片尺寸
3. 应用科技商业配色方案
4. 标准化字体和字号
5. 优化文本间距和对齐
6. 保存转换后的文件
7. 创建额外的母版模板文件

## 反馈和改进 / Feedback and Improvements

如有改进建议或发现问题，请在仓库中提交 Issue 或 Pull Request。

For suggestions or issues, please submit an Issue or Pull Request in the repository.

---

**License Note / 许可说明**: 本模板基于仓库中的现有文件创建，遵循仓库的许可协议。推荐的开源字体（Noto Sans CJK）遵循 SIL Open Font License。

## 参考截图 / Reference Screenshots

原始演示文稿的截图参考（用户提供）：

**Screenshot 1 - Simplified Layout:**
![Reference Screenshot 1](https://github.com/user-attachments/assets/92355ed7-27a9-4368-97d2-7b1f619368a5)

**Screenshot 2 - Full Slide with Details:**
![Reference Screenshot 2](https://github.com/user-attachments/assets/14719f49-9372-4584-82cd-a5f146a00792)

这些截图展示了科技商业风格的关键元素：
- 清晰的蓝色边框文本框
- 简洁的白色背景
- 专业的Q=P_fus/P_ext公式展示
- 科学挑战和工程挑战的对比布局
- 底部深蓝色强调条

