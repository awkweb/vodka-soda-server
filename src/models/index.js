import path from 'path';
import Sequelize from 'sequelize';

const basename = path.basename(module.filename);
const env = process.env.NODE_ENV || 'development';
const config = require(`${__dirname}/../config/database.config.json`)[env];
const db = {};

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable]);
} else {
  sequelize = new Sequelize({
    database: config.database,
    username: config.username,
    password: config.password,
    host: config.host,
    port: config.port,
    dialect: config.dialect,
    operatorsAliases: Sequelize.Op,
  });
}

const User = sequelize.define('User', {
  email: {
    allowNull: false,
    type: Sequelize.STRING,
    unique: true,
    validate: {
      isEmail: true,
    },
  },
  name: {
    allowNull: false,
    type: Sequelize.STRING,
  },
  age: {
    allowNull: false,
    type: Sequelize.INTEGER,
  },
  gender: {
    allowNull: false,
    type: Sequelize.STRING,
  },
  deletedAt: {
    type: Sequelize.DATE
  },
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

export default db;
