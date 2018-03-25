export default (sequelize, DataTypes) => {
  const User = sequelize.define('User', {
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      isEmail: true,
    },
    facebookAccessToken: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    facebookId: {
      allowNull: false,
      type: DataTypes.BIGINT,
    },
    gender: {
      type: DataTypes.STRING,
    },
    name: {
      allowNull: false,
      type: DataTypes.STRING,
    },
  });

  return User;
};
