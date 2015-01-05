var express = require('express');
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app = express();

app.get('/scrape', function(req, res){
    var url = 'http://scores.espn.go.com/ncb/scoreboard';
    
    request(url, function(error, response, html){
	if(!error){
	    var $ = cheerio.load(html);
	    
	    var team1, score1, team2, score2, status;//, team2, score1, score2, time;
	    var json = {team1: "", score1: "", team2: "", score2:"", status: ""}//, team2: "", score1: "", score2: "", time: ""};
	    
	    $('.visitor').filter(function(){
		var data = $(this);
		team1 = data.find('.team-name').text();
		score1 = data.find('.final').text();
		json.team1 = team1
		json.score1 = score1
	    })


	    $('.home').filter(function(){
		var data = $(this);
		team2 = data.find('.team-name').text();
		score2 = data.find('.final').text();
		json.team2 = team2
		json.score2 = score2
	    })
	    /*
	    $('.home').filter(function(){
		var data = $(this);
		team2 = data.find('team-name').text();
		json.team2 = team2
	    })
	    */
	    $('.game-status').filter(function(){
		var data = $(this);

		status = data.text();
		json.status = status
	    })
	}

	fs.writeFile('output.json', JSON.stringify(json, null, 4), function(err){
	    console.log('file successfully written!');
	})
	res.send("check your console!");
    })
})


app.listen('8081');
console.log('check port 8081');
exports = module.exports = app;
