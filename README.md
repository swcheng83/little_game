# little_game

用 Claude Code Cloud session 做的小遊戲集合，同時用來測試跨電腦同步。

## 遊戲

### 貪吃蛇 `index.html`

直接用瀏覽器打開 `index.html` 就能玩，不需要安裝任何東西。

- 方向鍵或 WASD 移動，空白鍵或 Enter 開始與暫停
- 手機可以用棋盤下方的方向鈕，或直接在棋盤上滑動
- 吃到紅色食物加 1 分，每 5 分加快一級
- 撞牆或撞到自己就結束，最高分會存在瀏覽器裡

想用網址直接玩的話，到 GitHub 的 Settings 裡的 Pages，把來源設成 main 分支的根目錄。

## 其他檔案

- `sync-test.txt`：Cloud session 容器裡建立的標記檔，記錄建立時間與 session ID。
