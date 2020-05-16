package com.example.myapplication;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewGroup.LayoutParams;
import android.widget.Switch;
import android.widget.TextView;

@SuppressWarnings("WeakerAccess")
public class JoyStickClass {

    private double position_x = 0.0, position_y = 0.0;
    private ViewGroup mLayout;
    private LayoutParams params;
    private int stick_width, stick_height;
    private DrawCanvas draw;
    private Paint paint;
    private Bitmap stick;
    private double exp_var=6*Math.sqrt(3);
    private boolean touch_state = false;
    private boolean layOutVar;


    JoyStickClass (Context context, ViewGroup layout, int stick_res_id,boolean layOut) {
        stick = BitmapFactory.decodeResource(context.getResources(), stick_res_id);
        stick_width = stick.getWidth();
        stick_height = stick.getHeight();
        layOutVar=layOut;
        draw = new DrawCanvas(context);
        paint = new Paint();
        mLayout = layout;
        initialisations();
    }

    private void initialisations(){
        params = mLayout.getLayoutParams();
        if(!layOutVar)
        {
            stick = Bitmap.createScaledBitmap(stick, 150, 150, false);
            params.width = 750;
            params.height = 750;
        }
        else
            stick = Bitmap.createScaledBitmap(stick, 90, 90, false);
        stick_width = stick.getWidth();
        stick_height = stick.getHeight();

        mLayout.getBackground().setAlpha(250);
        paint.setAlpha(1000);
        draw.position((double)params.width / 2,(double)params.height / 2);
        draw();
    }

    private void drawOnCanvas(double x,double y,boolean var,int x_var,TextView t1,TextView t2,TextView t3,MotionEvent arg1)
    {
        if(layOutVar)
            draw.position(arg1.getX() - position_x,y);
        else
            draw.position(x,y);
        draw();
        touch_state = var;
        if(x_var==1)
        {
            position_x=0.0;
            position_y=0.0;
        }
        if(!layOutVar)
        {
            String Vx="Vx: ",Vy="Vy: ",x1="",y1="";
            x1= String.valueOf(precision(position_x /exp_var));
            Vx+=x1;
            Vx+=" m/s";
            y1=String.valueOf(precision(-position_y /exp_var));
            Vy+=y1;
            Vy+=" m/s";
            t1.setText(Vx);
            t2.setText(Vy);
            new SendMessage().execute(x1+","+y1+",0");
        }

        else
        {
            String Vz="Vz: ",z1="";
            z1=String.valueOf(precision(-position_y /exp_var));
            Vz+=z1;
            Vz+=" m/s";
            t3.setText(Vz);
            new SendMessage().execute("0,0,"+z1);

        }

    }
    public void drawStick(MotionEvent arg1, TextView t1,TextView t2,TextView t3) {

        position_x = arg1.getX() - (double)params.width / 2;
        position_y = arg1.getY() - (double)params.height /2;

        double distance=Math.sqrt(position_x*position_x+position_y*position_y);

        if(arg1.getAction() == MotionEvent.ACTION_DOWN) {
            if (distance <= 300) {

                drawOnCanvas(arg1.getX(), arg1.getY(),true,0,t1,t2,t3,arg1);

            } else {

                drawOnCanvas(arg1.getX() - position_x, arg1.getY() - position_y,false,1,t1,t2,t3,arg1);

            }
        }
        else if(arg1.getAction() == MotionEvent.ACTION_MOVE && touch_state) {
            if(distance <= 300) {

                drawOnCanvas(arg1.getX(), arg1.getY(),true,0,t1,t2,t3,arg1);

            } else {

                drawOnCanvas(arg1.getX() - position_x, arg1.getY() - position_y,true,1,t1,t2,t3,arg1);

            }
        } else if(arg1.getAction() == MotionEvent.ACTION_UP) {

            drawOnCanvas(arg1.getX() - position_x, arg1.getY() - position_y,false,1,t1,t2,t3,arg1);

        }

    }

    private void draw() {
        try {
            mLayout.removeView(draw);
        } catch (Exception e) {
            System.out.println(e);
        }
        mLayout.addView(draw);
    }
    private class DrawCanvas extends View{
        double x, y;

        public DrawCanvas(Context context) {
            super(context);
        }

        public void onDraw(Canvas canvas) {
            canvas.drawBitmap(stick, (float)x, (float)y, paint);
        }

        private void position(double pos_x, double pos_y) {
            x = pos_x - ((double)stick_width / 2);
            y = pos_y - ((double)stick_height /2);
        }
    }
    public double precision(double input) {
        return Math.round(input * 10000) / 10000.0d;
    }
}

