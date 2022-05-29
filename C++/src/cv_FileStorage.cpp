/*
 * @Author: your name
 * @Date: 2022-02-07 14:25:34
 * @LastEditTime: 2022-02-07 15:31:07
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /learn_opencv/src/cv_FileStorage.cpp
 */
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <time.h>
#include <fstream>

using namespace std;
using namespace cv;

void write_yaml_opencv_mat();

void read_yaml_opencv_mat();

void read_txt_to_yaml(const string& txt_path);
void write_yaml(const string& yaml_path);

int main() {

    // read_yaml_opencv_mat();

    read_txt_to_yaml("/home/george/MY_LIB/PYTHON/calib_imu_to_cam.txt");

    // string mat_yaml_path = "/home/nuc02/MY_LIB/C++/mat.yaml";
    // write_yaml(mat_yaml_path);
    
    return 0;
}


void write_yaml_opencv_mat()
{
    FileStorage fs("/home/george/MY_LIB/C++/test.yaml", FileStorage::WRITE);

    fs << "frameCount" << 5;

    time_t rawtime; time(&rawtime);
    fs << "calibrationDate" << asctime(localtime(&rawtime));

    Mat cameraMatrix = (
            Mat_<float>(3,3)
                    << 1000, 0, 320, 0, 1000, 240, 0, 0, 1
            );

    Mat distCoeffs = (
            Mat_<float>(5,1)
                    << 0.1, 0.01, -0.001, 0, 0
            );

    fs << "cameraMatrix" << cameraMatrix << "distCoffes" << distCoeffs;

    fs << "features" << "[";
    for(int i = 0; i < 3; i++){
        int x = rand() % 640;
        int y = rand() % 480;
        uchar lbp = rand() % 256;

        fs << "{:" << "x" << x << "y" << y << "lbp" << "[:";
        for(int j = 0; j < 8; j++)
            fs << ((lbp >> j) & 1);
        fs << "]" << "}";
    }
    fs << "]";

    fs.release();
}

void read_yaml_opencv_mat()
{
    cv::FileStorage fs2("/home/george/MY_LIB/C++/opencv_mat.yaml", cv::FileStorage::READ);

    cv::Mat Tcb;
    fs2["Tcb"] >> Tcb;

    cout << Tcb << endl;
    cout << Tcb.type() << endl;

    fs2.release();

    cv::FileStorage fs3("/home/george/MY_LIB/C++/opencv_mat.yaml", cv::FileStorage::APPEND);

    cv::Mat Tbc = Tcb.inv();
    cout << Tbc.type() << endl;
    cout << Tbc << endl;
    fs3 << "Tbc" << Tbc;
    
    fs3.release();

}

void read_txt_to_yaml(const string& txt_path)
{
    fstream txt_f;
    txt_f.open(txt_path.c_str());

    cv::Mat Tcb(4, 4, CV_32F);
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            txt_f >> Tcb.at<float>(i, j);
        }
    }

    cout << Tcb << endl;
    cout << Tcb.type() << endl;

    cv::Mat Tbc = Tcb.inv();
    cout << Tbc << endl;
    cout << Tbc.type() << endl;

    cv::FileStorage fs("/home/george/MY_LIB/C++/calib_cam_to_imu.yaml", FileStorage::WRITE);

    fs << "Tbc" << Tbc;

    fs.release();


}

void write_yaml(const string& yaml_path)
{
    cv::Mat Tcb(4, 4, CV_32F);
    Tcb.at<float>(0, 0) = 1.0;
    Tcb.at<float>(0, 1) = 0.0;
    Tcb.at<float>(0, 2) = 0.0;
    Tcb.at<float>(0, 3) = 0.00552000012248755;
    Tcb.at<float>(1, 0) = 0.0;
    Tcb.at<float>(1, 1) = 1.0;
    Tcb.at<float>(1, 2) = 0.0;
    Tcb.at<float>(1, 3) = -0.00510000018402934;
    Tcb.at<float>(2, 0) = 0.0;
    Tcb.at<float>(2, 1) = 0.0;
    Tcb.at<float>(2, 2) = 1.0;
    Tcb.at<float>(2, 3) = -0.011739999987185;
    Tcb.at<float>(3, 0) = 0.0;
    Tcb.at<float>(3, 1) = 0.0;
    Tcb.at<float>(3, 2) = 0.0;
    Tcb.at<float>(3, 3) = 1.0;

    cv::FileStorage fs(yaml_path, FileStorage::WRITE);
    fs << "Tbc" << Tcb;
    fs.release();
    
}