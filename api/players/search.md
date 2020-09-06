# Search players by name

Get an array of player search results

**URL** : `/api/leaderboard/{game}/players/search`

**Method** : `GET`

**Parameters**: `?search=Campaign`


## Success Response

**Code** : `200 OK`


## Example Response (Results)
```json
[
   {
      "id": 1234,
      "player_name":"Player name",
      "rank":1,
      "wins":174,
      "losses":3,
      "points":1703.87
   }
]
```

## Example Response (No results)
```json
[]
```
