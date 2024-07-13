#ifndef DIALOGREC_H
#define DIALOGREC_H

#include <QDialog>
#include <QtWidgets>
namespace Ui {
class DialogRec;
}

class DialogRec : public QDialog
{
    Q_OBJECT

public:
    explicit DialogRec(QWidget *parent = nullptr);
    ~DialogRec();

private:
    Ui::DialogRec *ui;
};

#endif // DIALOGREC_H
