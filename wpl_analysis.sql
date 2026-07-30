-- ============================================================
-- WPL Data Analysis - SQL Script
-- Database: wpl_database.db (SQLite)
-- Table: matches
-- Run with: sqlite3 wpl_database.db < wpl_analysis.sql
-- Or open wpl_database.db in DB Browser for SQLite and run each block
-- ============================================================

-- 1. Table schema (for reference; table is created by build_database.py)
-- CREATE TABLE matches (
--     match_id        INTEGER PRIMARY KEY,
--     season          INTEGER,
--     date            TEXT,
--     team1           TEXT,
--     team2           TEXT,
--     venue           TEXT,
--     city            TEXT,
--     toss_winner     TEXT,
--     toss_decision   TEXT,
--     winner          TEXT,
--     win_by_runs     INTEGER,
--     win_by_wickets  INTEGER,
--     player_of_match TEXT
-- );

-- 2. Quick sanity check
SELECT COUNT(*) AS total_matches FROM matches;

-- 3. Matches played per season
SELECT season, COUNT(*) AS matches_played
FROM matches
GROUP BY season
ORDER BY season;

-- 4. Total wins per team (across all seasons)
SELECT winner AS team, COUNT(*) AS total_wins
FROM matches
GROUP BY winner
ORDER BY total_wins DESC;

-- 5. Win percentage per team
--    (wins / total matches played by that team, counting team1+team2 appearances)
SELECT
    t.team,
    COUNT(DISTINCT CASE WHEN m.winner = t.team THEN m.match_id END) AS wins,
    COUNT(m.match_id) AS matches_played,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN m.winner = t.team THEN m.match_id END)
          / COUNT(m.match_id), 2) AS win_pct
FROM (
    SELECT DISTINCT team1 AS team FROM matches
    UNION
    SELECT DISTINCT team2 AS team FROM matches
) t
JOIN matches m ON t.team = m.team1 OR t.team = m.team2
GROUP BY t.team
ORDER BY win_pct DESC;

-- 6. Toss impact: how often did the toss winner also win the match?
SELECT
    SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) AS toss_and_match_winner,
    SUM(CASE WHEN toss_winner != winner THEN 1 ELSE 0 END) AS toss_winner_lost,
    ROUND(100.0 * SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) / COUNT(*), 2) AS toss_win_pct
FROM matches;

-- 7. Toss decision trend (bat first vs field first)
SELECT toss_decision, COUNT(*) AS times_chosen
FROM matches
GROUP BY toss_decision;

-- 8. Matches hosted per venue
SELECT venue, city, COUNT(*) AS matches_hosted
FROM matches
GROUP BY venue, city
ORDER BY matches_hosted DESC;

-- 9. Average win margin by type (runs vs wickets)
SELECT
    ROUND(AVG(CASE WHEN win_by_runs > 0 THEN win_by_runs END), 2) AS avg_win_margin_runs,
    ROUND(AVG(CASE WHEN win_by_wickets > 0 THEN win_by_wickets END), 2) AS avg_win_margin_wickets
FROM matches;

-- 10. Season champions (final = last match of each season, by date)
SELECT season, winner AS champion, team1, team2, date
FROM matches m
WHERE date = (SELECT MAX(date) FROM matches WHERE season = m.season)
ORDER BY season;

-- 11. Most Player-of-the-Match awards
SELECT player_of_match, COUNT(*) AS awards
FROM matches
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 5;
