index = 0;
let cubes = [[[[true]]], [[[true, true]]]];
let initial_blocks = [
    new Steve(), new Steve(), new Steve(), new Steve(), new Steve(), new Steve(),
    new Carmen(), new Carmen(), new Carmen(), new Carmen(), new Carmen(), new Carmen(),
    new Unit(), new Unit(), new Unit(), new Unit(), new Unit(),
]
var len = 10;
var finder;

function setup() {
    createCanvas(600, 600, WEBGL);
    // noLoop();
    finder = new Search(
        new World(initial_blocks, null),
        30
    );
}

function draw() {
    background(200);
    rotateX(frameCount * 0.01);
    rotateY(frameCount * 0.01);

    plotcube(cubes[index]);
}

function plotcube(cube) {
    for (var x = 0; x < cube.length; x++) {
        for (let y = 0; y < cube[0].length; y++) {
            for (let z = 0; z < cube[0][0].length; z++) {
                if (cube[x][y][z]) {
                    push();
                    translate(x * len, y * len, z * len);
                    box(len);
                    pop();
                }
            }
        }
    }
}

function mousePressed(event) {
    finder.search();
    console.log(event);
}

function keyPressed() {
    index++;
    index %= cubes.length;
}