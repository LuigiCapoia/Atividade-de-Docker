import * as mongoose from 'mongoose';

export const databaseProviders = [
  {
    provide: 'DATABASE_CONNECTION',
    useFactory: async (): Promise<typeof mongoose> =>
      await mongoose.connect(process.env.MONGO_URI || 'mongodb://localhost:27017/user-crud', {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      }),
  },
];
