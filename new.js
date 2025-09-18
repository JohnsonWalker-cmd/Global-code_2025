require('dotenv').config();




let apiKey = process.env.WEATHER_KEY;


async function getCurrency(){
    try {
        const response  = await fetch(apiKey)
        if (!response.ok) throw new Error("data not found")
        const data =  await response.json() ;
        console.log(data)
    } catch(error){
        console.log("Error" , error)
    }
}
getCurrency();