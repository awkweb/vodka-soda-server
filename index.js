import express from 'express';
import bodyParser from 'body-parser';
import {
  graphiqlExpress,
  graphqlExpress,
} from 'graphql-server-express';
import { makeExecutableSchema } from 'graphql-tools';

import models from './models';
import resolvers from './resolvers';
import typeDefs from './type-defs';

const schema = makeExecutableSchema({resolvers, typeDefs});
const app = express();
app
  .use('/graphiql', graphiqlExpress({ endpointURL: '/graphql' }))
  .use('/graphql', bodyParser.json(), graphqlExpress({ schema, context: { models } }));

models.sequelize.sync()
  .then(() =>
    app.listen(4000, () =>
      console.log('Running a GraphQL API server at localhost:4000/graphql')));
