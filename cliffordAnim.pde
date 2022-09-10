final int maxIte = 10000000;
float a = 4, b = 1.2, c = -1.5, d = 1, e = 0, f = 0, g = 0;
PVector base = new PVector(0, 0);

ArrayList<PVector> points = new ArrayList<PVector>();
int ite = 0;
int frame = 0;

float maxX = 0, maxY = 0, maxZ = 0;
float minX = 0, minY = 0, minZ = 10;

void setup()
{
  size(800, 800, P2D);
  background(0);
  PVector origin = new PVector(0, 0);
  points.add(origin);
}

void draw()
{
  translate(400, 400);
  //scale(10);
  for (int i=0; i<1000; i++) {
    float oldx = base.x;
    float oldy = base.y;

    base.x = sin(a*oldy)+c*cos(a*oldx);
    base.y = sin(b*oldx)+d*cos(b*oldy);

    float x = map(base.x, -3, 3, -400, 400);
    float y = map(base.y, -3, 3, -400, 400);

    int r = floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2.7, 255, 0));
    int b = floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2.7, 0, 255));
    int g = 255 - (r+b)/4;
    colorMode(RGB);
    stroke(r, g, b, 50);

    point(x, y);
    ite++;
    //println(base.x, base.y);
    //println(x, y);
    
    if(base.x > maxX){maxX = base.x;}
    if(base.y > maxY){maxY = base.y;}
    //if(base.z > maxZ){maxZ = base.z;}
    if(base.x < minX){minX = base.x;}
    if(base.y < minY){minY = base.y;}
    ////if(base.z < minZ){minZ = base.z;}
    
  }
  //println(ite);
  //saveFrame("framestif/#######.tif");
  //frame++;
  //if(frame>899){noLoop();}
  //println(minX, maxX, minY, maxY);
}
