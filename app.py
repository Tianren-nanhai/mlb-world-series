import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 模擬 2026 年 MLB 世界大賽決賽賽程資料（採七戰四勝制）
    # 包含：欄位1(team_home/team_away), 欄位2(score_home/score_away), 欄位3(game_time)
    schedule_data = [
        {
            "game_name": "Game 1",
            "team_away": "紐約洋基 (Yankees)", "score_away": 4,
            "team_home": "洛杉磯道奇 (Dodgers)", "score_home": 3,
            "game_time": "2026-10-23 20:00 (EDT)"
        },
        {
            "game_name": "Game 2",
            "team_away": "紐約洋基 (Yankees)", "score_away": 1,
            "team_home": "洛杉磯道奇 (Dodgers)", "score_home": 5,
            "game_time": "2026-10-24 20:00 (EDT)"
        },
        {
            "game_name": "Game 3",
            "team_away": "洛杉磯道奇 (Dodgers)", "score_away": 4,
            "team_home": "紐約洋基 (Yankees)", "score_home": 2,
            "game_time": "2026-10-26 20:00 (EDT)"
        },
        {
            "game_name": "Game 4",
            "team_away": "洛杉磯道奇 (Dodgers)", "score_away": 11,
            "team_home": "紐約洋基 (Yankees)", "score_home": 4,
            "game_time": "2026-10-27 20:00 (EDT)"
        },
        {
            "game_name": "Game 5",
            "team_away": "洛杉磯道奇 (Dodgers)", "score_away": 7,
            "team_home": "紐約洋基 (Yankees)", "score_home": 6,
            "game_time": "2026-10-28 20:00 (EDT)"
        },
        {
            "game_name": "Game 6 (如有需要)",
            "team_away": "紐約洋基 (Yankees)", "score_away": "-",
            "team_home": "洛杉磯道奇 (Dodgers)", "score_home": "-",
            "game_time": "2026-10-30 20:00 (EDT)"
        },
        {
            "game_name": "Game 7 (如有需要)",
            "team_away": "紐約洋基 (Yankees)", "score_away": "-",
            "team_home": "洛杉磯道奇 (Dodgers)", "score_home": "-",
            "game_time": "2026-10-31 20:00 (EDT)"
        }
    ]
    return render_template('index.html', matches=schedule_data)

if __name__ == '__main__':
    # 讀取 Render 環境變數的 Port，若本地端執行則預設 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
