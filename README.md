# 📅 CalSync — ダブルブッキング防止カレンダー

## セットアップ

```bash
Bash
# 1. 仮想環境（名前は venv）を作成
python3 -m venv venv

# 2. 仮想環境を有効化（アクティベート）
source venv/bin/activate
Windows の場合
PowerShell
# 1. 仮想環境を作成
python -m venv venv
# 2. 仮想環境を有効化
.\venv\Scripts\activate
ブラウザで http://localhost:5000 を開く
pip install flask
# アプリの起動
python main.py


## デモアカウント

| ユーザー名 | パスワード | 表示名 |
|---|---|---|
| alice | password | アリス |
| bob | password | ボブ |
| carol | password | キャロル |

## ファイル構成

```
calendar_app/
├── main.py                 # Flaskエントリポイント
├── models.py               # データクラス定義
├── data.py                 # DB初期化・ユーティリティ
├── auth.py                 # ログイン・セッション管理
├── event_service.py        # 予定管理・ダブルブッキング判定
├── friend_service.py       # フレンド管理・検索
├── notification_service.py # 通知生成・既読管理
├── requirements.txt
├── templates/
│   └── index.html          # SPAメインHTML
└── static/
    ├── style.css           # ダークテーマCSS
    └── app.js              # フロントエンドJS
```

## 主な機能

- **カレンダー表示** — 月次カレンダー、イベントドット表示
- **ダブルブッキング検出** — 予定追加時にリアルタイム重複警告（入力中プレビュー）
- **予定管理** — 追加・削除、公開/非公開設定
- **フレンド機能** — ユーザー検索、フレンド申請・承認
- **参加可否回答** — 公開イベントに参加/不参加で回答
- **通知センター** — ダブルブッキング警告、フレンド申請、参加回答通知
- **レスポンシブ** — PC・スマホ対応

## 技術スタック

- **バックエンド**: Python / Flask / SQLite
- **フロントエンド**: Vanilla JS (SPA) / CSS3 / HTML5
- **認証**: セッションベース
- **DB**: SQLite（ファイルベース、追加設定不要）
