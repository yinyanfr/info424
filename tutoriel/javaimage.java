public abstract class AbstractImageCreator {  
    private static Random rnd = new Random(new Date().getTime());  
    private Drawer drawer;  
      
    //largeur d'image 
    private int width = 200;  
      
    //hauteur d'image 
    private int height = 80;  
      
    //border couleur
    private Color rectColor;  
      
    //bg couleur 
    private Color bgColor;  
      
      
    //format d'image
    private String formatName = "ppm";  
      
      
    //文字旋转的弧度数  
    private double radian = 0;  
    private double rotateX = 0;  
    private double rotateY = 0;  
      
    //缩放  
    private double scale = 1;  
      
  
    //##### 此处省略getter、setter方法 #####  
  
  
    public AbstractImageCreator(Drawer drawer){  
        this.drawer = drawer;  
    }  
      
    /** 
     * 画干扰线 
     */  
    private void drawRandomLine(Graphics graph){  
        for(int i=0;i<lineNum;i++){  
            //线条的颜色  
            graph.setColor(getRandomColor(100, 155));  
              
            //线条两端坐标值  
            int x1 = rnd.nextInt(width);  
            int y1 = rnd.nextInt(height);  
              
            int x2 = rnd.nextInt(width);  
            int y2 = rnd.nextInt(height);  
              
            //画线条  
            graph.drawLine(x1, y1, x2, y2);  
        }  
    }  
      
    /** 
     * 随机获取颜色对象 
     */  
    private Color getRandomColor(int base, int range){  
        if((base + range) > 255) range = 255 - base;  
          
        int red = base + rnd.nextInt(range);  
        int green = base + rnd.nextInt(range);  
        int blue = base + rnd.nextInt(range);  
          
        return new Color(red, green, blue);  
    }  
      
    public void generateImage(String text)throws IOException{  
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);  
          
        if(rectColor == null) rectColor = new Color(0, 0, 0);  
        if(bgColor == null) bgColor = new Color(240, 251, 200);  
          
        //获取画布  
        Graphics2D g = (Graphics2D)image.getGraphics();  
          
        //画长方形  
        g.setColor(bgColor);  
        g.fillRect(0, 0, width, height);  
          
        //外框  
        g.setColor(rectColor);  
        g.drawRect(0, 0, width-1, height-1);  
          
          
        //执行  
        g.dispose();  
          
        //输出图片结果  
        saveImage(image);  
    }  
      
    protected abstract void saveImage(BufferedImage image)throws IOException;  
      
}  







/////////////////////////////////////////////////////////////////////////////////////////////////////////
    public class FileImageCreator extends AbstractImageCreator {  
        private String fileName;  
          
        public String getFileName() {  
            return fileName;  
        }  
      
        public void setFileName(String fileName) {  
            this.fileName = fileName;  
        }  
      
        public FileImageCreator(Drawer drawer){  
            super(drawer);  
        }  
          
        public FileImageCreator(Drawer drawer, String fileName){  
            super(drawer);  
            this.fileName = fileName;  
        }  
          
        @Override  
        protected void saveImage(BufferedImage image)throws IOException{  
            ImageIO.write(image, getFormatName(), new File(fileName));  
        }  
    }  
