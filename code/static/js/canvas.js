var game = new Phaser.Game(1200, 600, Phaser.AUTO, 'pantalla', { preload: preload, create: create, update: update });

var bricks;
var player01;
var controllers;

function create_up_wall()
{
    for (var count = 0; count < 50; count++ )
    {
        var brick = bricks.create(0 + count * 30, 30, "brick");
        brick.body.immovable = true;
    }
}

function create_botton_wall()
{
    for (var count = 0; count < 50; count++ )
    {
        var brick = bricks.create(0 + count * 30, 570, "brick");
        brick.body.immovable = true;
    }
}

function create_left_wall()
{
    for (var count = 0; count < 20; count++ )
    {
        var brick = bricks.create(0, 0 + count * 30, "brick");
        brick.body.immovable = true;
    }
}

function create_right_wall()
{
    for (var count = 0; count < 20; count++ )
    {
        var brick = bricks.create(1170, 0 + count * 30, "brick");
        brick.body.immovable = true;
    }
}

function create_bricks()
{
    create_up_wall();
    create_botton_wall();
    create_left_wall();
    create_right_wall();


    for (var count = 0; count < 5; count++ )
    {
        var brick = bricks.create(200, 200 + count * 30, "brick");
        brick.body.immovable = true;
    }

    for (var count = 0; count < 5; count++ )
    {
        var brick = bricks.create(1000, 200 + count * 30, "brick");
        brick.body.immovable = true;
    }

}


function preload() 
{
    game.load.image('brick', 'img/brick.png');

    game.load.spritesheet('player-01', 'img/player01.png', 50, 50);
    
}

function create() 
{
    //fisica
    game.physics.startSystem(Phaser.Physics.ARCADE);

    bricks = game.add.group();
    bricks.enableBody = true;
    create_bricks();


    //add player-01

    player01 = game.add.sprite(50, 500, "player-01");
    game.physics.arcade.enable(player01);

    player01.animations.add("izquierda", [0], 10, true);
    player01.animations.add("arriba", [1], 10, true);
    player01.animations.add("abajo", [2], 10, true);
    player01.animations.add("derecha", [3], 10, true);

    //game.add.sprite(200, 20, 'brick');


    //game.add.sprite(600, 20, 'game');

    controllers = game.input.keyboard.createCursorKeys();
}


function ARRIBA()
{
    player01.body.velocity.y = -50;
    player01.body.velocity.x = 0;
    player01.animations.play("arriba");
}


function update() 
{
   // Con los grupos marte.physics.arcade.collide();

   game.physics.arcade.collide(player01, bricks);

   //player01.body.velocity.x = 0;
   //player01.body.velocity.y = 0;
   

   if (controllers.left.isDown)
   {
        player01.body.velocity.x = -50;
        player01.body.velocity.y = 0;
        player01.animations.play("izquierda");
   }
   
   if (controllers.right.isDown)
   {
        player01.body.velocity.x = +50;
        player01.body.velocity.y = 0;
        player01.animations.play("derecha");
   }
   
   if (controllers.up.isDown)
   {
        player01.body.velocity.y = -50;
        player01.body.velocity.x = 0;
        player01.animations.play("arriba");
   }
   
   if (controllers.down.isDown)
   {
        player01.body.velocity.y = +50;
        player01.body.velocity.x = 0;
        player01.animations.play("abajo");
   }

   ARRIBA();


}