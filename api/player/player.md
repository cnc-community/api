# Get player by id

Get a players profile by player id

**URL** : `/api/leaderboard/{game}/player/{id}`

**Method** : `GET`

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

```