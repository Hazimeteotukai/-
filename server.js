// server.js
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// 機密情報
const correctPassword = '12';
const webhookUrl = 'https://discord.com/api/webhooks/1223447142740262972/vxrn9O3gB3fVm0mx0g_VcN4jYB0MRK-L6pdcinnad2gTAk3jFYbYg_S1vfPixzFLoK6G';
const redirectUrl = 'https://github.com/Hazimeteotukai/scriptdownloadsite/raw/main/Janru1.lua';

app.use(bodyParser.json());

// 静的ファイルを提供するための設定
app.use(express.static(path.join(__dirname, 'public')));

app.post('/send', (req, res) => {
    const { name, password } = req.body;

    if (password === correctPassword) {
        axios.post(webhookUrl, { content: name })
            .then(response => {
                res.status(200).json({ message: '送信成功!', redirect: redirectUrl });
            })
            .catch(error => {
                console.error('Error:', error);
                res.status(500).send('送信失敗!');
            });
    } else {
        res.status(401).send('パスワードが正しくありません。');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
