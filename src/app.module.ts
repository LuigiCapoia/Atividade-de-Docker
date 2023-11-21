import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { UserModule } from './user/user.module';
import { databaseProviders } from './database.config';

@Module({
  imports: [MongooseModule.forRoot('mongodb://0.0.0.0/nest'), UserModule],
  controllers: [],
  providers: [...databaseProviders],
})
export class AppModule {}
