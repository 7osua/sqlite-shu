SELECT trackid,
       name,
       bytes
FROM tracks
ORDER BY bytes DESC
LIMIT 10;