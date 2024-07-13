#include "consolewidget.h"

ConsoleWidget::ConsoleWidget(QWidget *parent) : QWidget(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);
    outputArea = new QTextEdit(this);
    outputArea->setReadOnly(true);
    outputArea->setStyleSheet("background-color: black; color: white; font-family: 'Courier New'; font-size: 12pt;");
    layout->addWidget(outputArea);
    setLayout(layout);
}

void ConsoleWidget::appendText(const QString &text)
{
    outputArea->append("<span style=\"color: green;\">" + text + "</span>");
}
