import peasy.*;
PeasyCam cam;

final int maxIte = 10000000;
float a = -5, b = -4.15, c = -3.1, d = -5, e = 2.27, f = -1.24, g = 0;
//float a = -5, b = -4.15, c = -3.1, d = -5, e = 1, f = 1, g = 0;

PVector base = new PVector(0, 0);

float maxX = 0, maxY = 0, maxZ = 0;
float minX = 10, minY = 10, minZ = 10;

//ArrayList<PVector> points = new ArrayList<PVector>();
int ite = 0;
int frame = 0;
void setup()
{
  size(800, 800, P3D);
  
  cam = new PeasyCam(this, 1000);
  
  background(0);
}

void draw()
{
  //translate(400, 400);
  //scale(10);
  for (int i=0; i<2000; i++) {
    float oldx = base.x;
    float oldy = base.y;
    float oldz = base.z;

    base.x = sin(a*oldy)-cos(b*oldx);
    base.y = sin(c*oldx)-cos(d*oldy);
    //base.z = oldy*sin(e*oldz)+cos(f*oldx);
    base.z = sin(e * oldx) - cos(f * oldz);
    
    float x = map(base.x, -2.5, 2.5, -400, 400);
    float y = map(base.y, -2.5, 2.5, -400, 400);
    float z = map(base.z, -1.5, 3.25, -400, 400);

    int r = floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2, 255, 0));
    int b = floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2, 128, 255));
    int g = 128 - ((r+b)/4);
    int opa = 25;//floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2, 5, 3));
    //int g = floor(map(abs(dist(base.x, base.y, 0, 0)), 0, 2, 128, 0));;
    colorMode(RGB);
    //strokeWeight(1);
    stroke(r,g,b, opa);
    //stroke(255); 
    //strokeWeight(10);
    point(x, y, z);
    ite++;
    
    if(base.x > maxX){maxX = base.x;}
    if(base.y > maxY){maxY = base.y;}
    if(base.z > maxZ){maxZ = base.z;}
    if(base.x < minX){minX = base.x;}
    if(base.y < minY){minY = base.y;}
    if(base.z < minZ){minZ = base.z;}
    
    //println(base.x, base.y, base.z);
    //println(x, y);
    //println(maxX, maxY, maxZ, minX, minY, minZ);
    
  }
  //println(ite/1000000);
  //saveFrame("framestifdejong/#####.tif");
  frame++;
  println(frame);
  //if(frame>899){noLoop();}
}

void mousePressed()
{
  background(0);
  noLoop(); 
}

void mouseReleased()
{
  loop(); 
}
