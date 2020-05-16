package com.example.myapplication;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.app.Activity;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.CompoundButton;
import android.widget.RelativeLayout;
import android.widget.Switch;
import android.widget.TextView;


public class MainActivity extends Activity {
    RelativeLayout layout_joystick,slider_z;
    TextView textView1, textView2, textView3;
    Switch sw;
    public JoyStickClass js,js_slider;

    @SuppressLint("ClickableViewAccessibility")
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sw = findViewById(R.id.switch1);
        textView1 = findViewById(R.id.textView1);
        textView2 = findViewById(R.id.textView2);
        textView3 = findViewById(R.id.textView3);
        slider_z = findViewById(R.id.slider);
        layout_joystick = findViewById(R.id.joystick);
        slider_z.setVisibility(View.GONE);
        js = new JoyStickClass(getApplicationContext(),layout_joystick, R.drawable.image_button,false);
        js_slider = new JoyStickClass(getApplicationContext(),slider_z, R.drawable.image_button,true);

        sw.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(!isChecked){
                    slider_z.setVisibility(View.GONE);
                }else{
                    slider_z.setVisibility(View.VISIBLE);
                    slider_z.setOnTouchListener(new OnTouchListener() {

                        public boolean onTouch(View arg0, MotionEvent arg1) {
                            js_slider.drawStick(arg1,textView1,textView2,textView3);
                            return true;
                        }

                    });
                }
            }
        });
        layout_joystick.setOnTouchListener(new OnTouchListener() {

            public boolean onTouch(View arg0, MotionEvent arg1) {
                js.drawStick(arg1,textView1,textView2,textView3);
                return true;
            }

        });
    }
}