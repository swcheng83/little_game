# little_game

用 Claude Code Cloud session 做的小遊戲集合，同時用來測試跨電腦同步。

## 遊戲

### 貪吃蛇 `index.html`

直接用瀏覽器打開 `index.html` 就能玩，不需要安裝任何東西。

- 方向鍵或 WASD 移動，空白鍵或 Enter 開始與暫停
- 手機可以用棋盤下方的方向鈕，或直接在棋盤上滑動
- 吃到紅色食物加 1 分，每 5 分加快一級
- 撞牆或撞到自己就結束，最高分會存在瀏覽器裡

線上版：https://swcheng83.github.io/little_game/ 。每次 push 到 main，GitHub Actions 會自動重新部署。

### 日常開圖 `dailymap/`

真實世界探索遊戲的手機網頁原型：一次一則傳聞加冷熱羅盤，走到 75 公尺內自動揭曉；可以在你站的地方埋傳聞，用連結傳給朋友。定位只在頁面開著時使用，資料只存在各自手機的瀏覽器。

線上版：https://swcheng83.github.io/little_game/dailymap/

- 第一次打開會先說明為什麼要定位，再請 Safari 問你；不開定位也能玩，到了按「我到了」。
- 從 LINE 打開時會提醒改用 Safari。
- `r/s01.html`～`r/s12.html`：12 則城市傳聞各自的分享頁，貼到 Threads 會帶出專屬預覽圖（`og/`）。圖由 `tools/make_og.py` 產生。
- 朋友埋的傳聞可以「存成圖片」傳 LINE；圖片只是預告，朋友要點連結才收得到傳聞。

## 其他檔案

- `sync-test.txt`：Cloud session 容器裡建立的標記檔，記錄建立時間與 session ID。
