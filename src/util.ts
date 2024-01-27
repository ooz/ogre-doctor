import * as Phaser from "../lib/phaser.min.js"

export function getParameters() {
    let url = new URL(window.location.href)
    let gameId = url.searchParams.get('gameId') || createGameId();
    let singlePlayer: string | boolean = url.searchParams.get('sp') || 'false';
    singlePlayer = (singlePlayer == 'true') ? true : false;
    let player = 'screen';
    let playerId = 'screen'
    if (gameId.startsWith('pp_')) {
        gameId = gameId.substr(3);
        player = 'pp';
        playerId = createGameId();
        singlePlayer = false;
    }
    if (gameId.startsWith('sp_')) {
        gameId = gameId.substr(3);
        player = 'sp';
        playerId = createGameId();
        singlePlayer = true;
    }
    return {
        'gameId': gameId,
        'player': player,
        'playerId': playerId,
        'singlePlayer': singlePlayer
    }
}

function createGameId() {
    // From https://gist.github.com/6174/6062387
    return [...Array(64)].map(i=>(~~(Math.random()*36)).toString(36)).join('')
}

export function get(id: string) {
    return document.getElementById(id)
}

export function removeElement(elemId: string) {
    let toRemove = get(elemId);
    toRemove?.parentNode?.removeChild(toRemove);
}

export function random(min, max) {
    return Phaser.Math.RND.between(min, max);
}
