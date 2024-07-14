QT       += core gui webenginewidgets
QT       += network


greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    dialogfilerec.cpp \
    dialogrec.cpp \
    dialogtoolrec.cpp \
    main.cpp \
    mainwindow.cpp \
    scaledpixmap.cpp

HEADERS += \
    dialogfilerec.h \
    dialogrec.h \
    dialogtoolrec.h \
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
