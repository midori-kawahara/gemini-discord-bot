# gemini-discord-bot

これは簡易的なDiscordチャットボットです。Geminiとの会話機能が実装されています。
@konoka-iori が個人的に使用するために作成されました。主に小規模なDiscordサーバーでの利用を想定しています。
Gemini APIを使ったDiscordのチャットボット作ってみたいよという人はぜひ参考にしてみてくださいね。

# コマンド一覧(機能一覧)

- `/about`: BOTの説明を表示します。
- `/chat`: Geminiとチャットができます。一問一答方式で、会話履歴は保存されません。使用されるモデルは `gemini-pro` です。

# 使い方

1. このリポジトリをクローンします。
2. `.env.sample` を `.env` にリネームします。
3. `.env` の `DISCORD_TOKEN` にDiscordのBOTのトークンを入力します。
4. `.env` の `GEMINI_API_KEY` にGeminiのAPI Keyを入力します。
5. `.env` の `DISCORD_SERVER_ID` にBOTを使用したいDiscordサーバーのIDを入力します。
6. `bot.py` を実行します。
7. BOTがログインできたのが確認できたら、Discordで `/about` と入力してみましょう！( `/chat` も動くはず。)

# ブランチについて

- `main`: 動作確認済みのブランチです。
- `develop`: 開発用のブランチです。こちらは動作確認が行われていません。
- `add/`: New Featureブランチです。新機能などの追加に使用します。`develop` から派生。
- `improvement/`: Improvement用ブランチです。既存の機能の改善に使用します。`develop` から派生。

# 注意事項

- このBOTは個人利用を想定して作成されています。
- このBOTはDiscordで動くものです。DiscordのアカウントやBOTの作成方法、サーバーの作成方法などについては公式サイト等を確認してください。
- このBOTはGemini APIを利用しています。Geminiの概要、APIの利用方法・API Keyの取得などについては公式サイト等を確認してください。
- このプロジェクトはみんな大好きMITライセンスです。BOTを使うときは自己責任で、かつこのリポジトリのURLを明記してください。詳細はLICENSEをご覧ください。
- 不具合報告、機能追加要望などはIssueください。Pull Requestも歓迎です！
