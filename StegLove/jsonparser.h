#ifndef JSONPARSER_H
#define JSONPARSER_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>

class JsonParser : public QObject {
    Q_OBJECT

public:
    explicit JsonParser(QWidget *parent = nullptr);
    void fetchJson(const QUrl &url);

signals:
    void jsonParsed(const QJsonObject &jsonObject);

private slots:
    void onNetworkReply(QNetworkReply *reply);

private:
    QNetworkAccessManager *networkManager;
    QWidget *parentWidget;
};

#endif // JSONPARSER_H
