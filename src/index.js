import express from 'express';
import logger from 'morgan';
import bodyParser from 'body-parser';
import router from './router';
import models from './models';

const app = express();
app.use(logger('dev'));
app.use(bodyParser.json());
app.use('/v1', router);

const port = process.env.PORT || 4000;

app.listen(port, () => console.log(`Server running on http://localhost:${port}`));
