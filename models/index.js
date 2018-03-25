import Sequelize from 'sequelize';

const sequelize = new Sequelize({
  database: 'vodka-soda',
  username: 'tom',
  password: null,
  dialect: 'postgres',
  operatorsAliases: Sequelize.Op,
});

const db = {
  User: sequelize.import('./user'),
};

Object
  .keys(db)
  .forEach((modelName) => {
    if ('associate' in db[modelName]) {
      db[modelName].associate(db);
    }
  });

db.sequelize = sequelize;

export default db;
