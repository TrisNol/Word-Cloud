const runtimeEnv = (window as Window & { env?: { apiUrl?: string } }).env;

export const environment = {
  production: true,
  apiUrl: runtimeEnv?.apiUrl || 'http://localhost:3000',
};
