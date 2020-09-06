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
      "player_name":"Campaign Player",
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