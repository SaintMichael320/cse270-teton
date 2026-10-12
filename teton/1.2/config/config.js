const LAT = "43.8866";
const LON = "-111.6777";
const APIKEY = "7cd1d6728c7c950dc18e9f981146ef04";

// Weather Setup
const WEATHER_URL_STUB = "./data/weather.json";
const WEATHER_URL_PROD = `https://api.openweathermap.org/data/2.5/weather?lat=${LAT}&lon=${LON}&appid=${APIKEY}`;

// Directory Setup
const DIRECTORY_DATA_URL_PROD = "<PRODUCTION_URL_HERE>";
const DIRECTORY_DATA_URL_STUB = "./data/business.json";
const DIRECTORY_DATA_URL_TEST = "http://127.0.0.1:8000/data/all";

// EXPORT THE VARIABLES PROPERLY USING CONST
const apiURL = WEATHER_URL_PROD;
const businessDataUrl = DIRECTORY_DATA_URL_TEST;