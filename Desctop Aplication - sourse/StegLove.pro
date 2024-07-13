QT       += core gui
QT       += core network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    consolewidget.cpp \
    dialogfilerec.cpp \
    dialogrec.cpp \
    dialogtoolrec.cpp \
    jsonfilter.cpp \
    jsonparser.cpp \
    main.cpp \
    mainwindow.cpp \
    scaledpixmap.cpp

HEADERS += \
    consolewidget.h \
    dialogfilerec.h \
    dialogrec.h \
    dialogtoolrec.h \
    jsonfilter.h \
    jsonparser.h \
    mainwindow.h \
    scaledpixmap.h

FORMS += \
    dialogfilerec.ui \
    dialogrec.ui \
    dialogtoolrec.ui \
    mainwindow.ui

win32:RC_FILE = file2.rc

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
