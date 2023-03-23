# Launchpad: apis/wordnik
API for dictionary and word of the day: https://developer.wordnik.com/

# API
  * [API Documentation](https://developer.wordnik.com/gettingstarted)

# Example
```
  export WORDNIK_API_KEY=yourkey
  curl -L http://api.wordnik.com/v4/words.json/randomWord?api_key=${WORDNIK_API_KEY}
```

  * Note: `-L` flag is required to follow redirects
  `
