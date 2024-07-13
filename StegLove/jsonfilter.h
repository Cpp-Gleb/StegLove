#ifndef JSONFILTER_H
#define JSONFILTER_H
#include <QCoreApplication>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonValue>
#include <QUrl>
#include <QObject>
#include <QDebug>

class JsonPostRequester : public QObject
{
    Q_OBJECT

public:
    JsonPostRequester(QObject *parent = nullptr);
    void sendPostRequest(const QUrl &url, const QJsonObject &json);
private slots:
    void onFinished(QNetworkReply *reply);
    void onError(QNetworkReply::NetworkError code);
private:
    QNetworkAccessManager manager;
    QJsonObject jsonResponse;
};

#endif // JSONFILTER_H
