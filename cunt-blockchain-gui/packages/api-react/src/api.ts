import { createApi } from '@reduxjs/toolkit/query/react';
import cuntLazyBaseQuery from './cuntLazyBaseQuery';

export const baseQuery = cuntLazyBaseQuery({});

export default createApi({
  reducerPath: 'cuntApi',
  baseQuery,
  endpoints: () => ({}),
});
