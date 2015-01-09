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
	    
	    $('div.mod-content').each(function(i, element){
		var game = $(this);
		var vTeam = game.find('.visitor').find('.team-name').text();
		//var vScore = game.find('.visitor').find('.final');
		var hTeam = game.find('.home').find('.team-name').text();
		//var status = game.find('.game-status').text();
		var gamedata = {
		    vTeam: vTeam,
		    hTeam: hTeam
		};
		console.log(gamedata);
	    });	    
	}
    })
})


app.listen('8081');
console.log('check port 8081');
exports = module.exports = app;
