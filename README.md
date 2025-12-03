# emoji-swap-verify

Emoji Swap Verify 是一个 3x3 “一步三连” 小游戏：每局只有一次交换机会，并且只有唯一解。桌面和移动端自适应，统计保存在浏览器本地。

## Live Demo

- https://emoji.closeai.moe

## 功能特性

- 唯一解棋盘生成（含横/竖/斜线三连验证，生成超时会提示重试）
- 点击-点击交换；失败回滚同一题，成功自动换题
- 成绩统计（wins/total/成功率）存储于 `localStorage`
- 规则说明模态；清除记录、换一题控件
- 深色、移动优先的居中卡片布局

## 使用方式

这是纯静态网页，直接打开 `index.html` 即可；或用任意静态服务器托管根目录（如 `npx serve .`）。

## 资源说明

- 表情素材来自 [Twemoji](https://github.com/twitter/twemoji)，遵循 CC-BY 4.0。
- 本项目其他代码与内容使用 MIT License。
