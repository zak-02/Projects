import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';

class MainPage extends StatelessWidget {
  const MainPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Select your outfit',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        leading: Container(
          margin: EdgeInsets.all(10),
          decoration: BoxDecoration(
          ),
          child: Transform.translate(
            offset: Offset(1, 1),
            child: SvgPicture.asset('assets/icons/black-circle.svg'),
          ),
        ),
      ),

      // Main body with stick man and squares underneath
      body: Center(
        child: Transform.translate(
          offset: Offset(0, -50),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Stick man SVG
              SvgPicture.asset(
                'assets/icons/stick-man.svg',
                height: 350,
                width: 120,
              ),

              SizedBox(height: 50), // spacing between stick man and first row

              // First row of squares
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                  SizedBox(width: 10),
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                  SizedBox(width: 10),
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                ],
              ),

              SizedBox(height: 30), // spacing between rows

              // Second row of squares
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                  SizedBox(width: 10),
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                  SizedBox(width: 10),
                  SvgPicture.asset(
                    'assets/icons/black-square-box.svg',
                    height: 80,
                    width: 80,
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
