$(document).ready(function(){
    console.log("ready")
    $("#result").hide()
    $("#errorDiv").hide();
    $("#loader").hide()
})

var submitFunction = function(){
    event.preventDefault();
    $("#result").hide()
    $("#errorDiv").hide();
    $("#loader").show()
    console.log("clicked", $("#stockName").val())
    $.ajax({ 
        type:"POST",
        url: document.location.origin+"/api/stock",
        data: JSON.stringify({"name":($("#stockName").val()).toUpperCase()}), 
        contentType: 'application/json',
        success: generateUI,
        error: function(xhr, status, err) {
            console.error(xhr, status, err.toString());
        }.bind(this)
    });  
}

generateUI = function(responseData){
    responseData = JSON.parse(responseData)
    $("#loader").hide();
    if(responseData.error === undefined){
        $("#errorDiv").hide();
        $("#result").show()
        generateStockPriceUI(responseData.stockPrice)
        generateNewsUI(responseData.news.news)
        generateFinancialNumbers(responseData.finiancialNumbers)
        generateEarningCalls(responseData.earningCalls)
    } else {
        generateErrorData(responseData.error)
    }
    
}

var generateErrorData = function(errorData){
    $("#result").hide()
    $("#errorDiv").show()
    $("#errorMessage").text(errorData)
}
var generateStockPriceUI = function(stockPriceData){
    console.log(stockPriceData)
    $("#stockPriceOpen").text(stockPriceData["1. open"])
    $("#stockPriceHigh").text(stockPriceData["2. high"])
    $("#stockPriceLow").text(stockPriceData["3. low"])
    $("#stockPriceClose").text(stockPriceData["4. close"])
    $("#stockPriceVolume").text(stockPriceData["5. volume"])
}

var generateNewsUI = function(newsData){
    // console.log(newsData)
    $("#news").empty()
    news =`<ol>`
    for (let i =0; i< 10; i++){
        if(newsData[i].sentiment == 0){
            eachNews = `<li>
            <a href="${newsData[i].url}" class="negativeSentiment" target="_blank">${newsData[i].title}</a>
            </li>`
        }
        else {
            eachNews = `<li>
            <a href="${newsData[i].url}" class="positiveNews" target="_blank">${newsData[i].title}</a>
        </li>`
        }
        
        news += eachNews
        // console.log(newsData[i])
    }
    news += `</ol>`
    $("#news").append(news)

}

var generateFinancialNumbers = function(financialData){
    $("#marketCap").text(financialData["market_cap"])
    $("#netCashFlowOp").text(financialData["net_cash_flow_op"])
    $("#netAshFlowFin").text(financialData["net_ash_flow_fin"])
    $("#netCashFlowInv").text(financialData["net_cash_flow_inv"])
    $("#lastYearRevenue").text(financialData["last_year_revenue"])


}
var generateEarningCalls = function(earningCallData){
    $("#earningCallData").empty()
    console.log("earning callsis ", earningCallData)
    
    var time = `<div class="col-sm-12"><span class="lead">Time of Call: ${earningCallData[1]}</span></div>
    <div class="col-sm-12" ><span class="lead">List of participants </span></div>`
    var people = earningCallData[0]

    $("#earningCallData").append(time)
    peopleString ='<div class="col-sm-12"><ol>'

    for (let i=0; i< people.length;i++){
        peopleString += `<li><span>${people[i]}</span></li>`
    }
    peopleString += '</ol></div>'
    $("#earningCallData").append(peopleString)
}